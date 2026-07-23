PROMPT_TEMPLATE = """
You are an industrial quality assurance inspector.

The following defects were detected on a steel surface:

{detections}

Generate a professional inspection report in the following format:

Inspection Report

Inspection Date:
(Current Date)

Detected Defects:
(List defects with confidence)

Summary:
(Brief description)

Severity:
(Low / Medium / High)

Recommended Action:
- Action 1
- Action 2
- Action 3

Keep the report concise and professional.
"""