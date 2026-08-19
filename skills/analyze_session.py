#!/usr/bin/env python3
# Memory-safe JSONL session analyzer – Codex session format
import sys, json, argparse

def extract_text_from_content(content):
    """Convert content array to plain text, skipping permission/collaboration blocks."""
    if not isinstance(content, list):
        return ""
    texts = []
    for item in content:
        if item.get("type") == "input_text":
            t = item.get("text", "")
            # skip huge instruction blocks that are not actual user/assistant messages
            if "<permissions instructions>" in t or "<collaboration_mode>" in t or "<apps_instructions>" in t or "<skills_instructions>" in t or "<plugins_instructions>" in t or "<environment_context>" in t:
                continue
            texts.append(t)
    return "\n".join(texts)

def analyze(filepath, limit=None):
    total_lines = 0
    first_user_msg = None
    last_assistant_msg = None
    user_messages = []
    findings = []
    tool_calls = []
    model = None
    turn_ids = []

    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if limit and total_lines >= limit:
                    break
                total_lines += 1
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue

                rtype = record.get("type", "")
                payload = record.get("payload", {})

                # capture model info from turn_context
                if rtype == "turn_context" and isinstance(payload, dict):
                    model = payload.get("model", model)
                    turn_id = payload.get("turn_id")
                    if turn_id:
                        turn_ids.append(turn_id)

                # handle response_item records (user, assistant, developer)
                if rtype == "response_item" and isinstance(payload, dict):
                    role = payload.get("role", "")
                    content = payload.get("content", "")
                    text = extract_text_from_content(content)
                    if not text:
                        continue
                    if role == "user":
                        if first_user_msg is None:
                            first_user_msg = text[:500]
                        user_messages.append(text[:500])   # store first 500 chars to keep memory low
                    elif role == "assistant":
                        last_assistant_msg = text[:1000]
                        # heuristic: detect findings
                        if any(kw in text.lower() for kw in ["vulnerability", "finding", "severity", "exploit", "bug", "critical", "high", "medium", "low", "submit-worthy"]):
                            findings.append(text[:500])
                    # tool calls might be embedded in assistant messages or separate
                    if "tool" in text.lower() or "function_call" in text:
                        tool_calls.append(text[:200])

                # capture tool call records if they exist directly
                if rtype == "tool_call" or rtype == "function_call":
                    tool_calls.append(str(payload)[:200])

    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        return
    except Exception as e:
        print(f"ERROR: {e}")
        return

    # print summary
    print("=== Session Summary ===")
    print(f"Lines processed: {total_lines}")
    print(f"Model: {model or 'unknown'}")
    print(f"Turn count: {len(turn_ids)}")
    print(f"First user message: {first_user_msg[:200] if first_user_msg else 'N/A'}...")
    print(f"Total user questions: {len(user_messages)}")
    print(f"Tool calls detected: {len(tool_calls)}")
    print(f"Potential findings extracted: {len(findings)}")
    print(f"Last assistant response (truncated): {last_assistant_msg[:500] if last_assistant_msg else 'N/A'}...")
    print("\n--- All User Questions (first 300 chars each) ---")
    for i, msg in enumerate(user_messages, 1):
        print(f"{i}. {msg[:300]}")
    if findings:
        print("\n--- Findings (first 5, truncated) ---")
        for i, f in enumerate(findings[:5], 1):
            print(f"Finding {i}: {f[:300]}...")
    if tool_calls:
        print("\n--- Tool Calls (first 5) ---")
        for t in tool_calls[:5]:
            print(t[:200])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    analyze(args.filepath, args.limit)
