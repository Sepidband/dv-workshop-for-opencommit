def render_content(codelab):
    buffer = []

    buffer.append(f"<google-codelab codelab-title=\"{codelab.title}\">")

    for step in codelab.steps:
        buffer.append(f"<google-codelab-step label=\"{step.label}\">{step.content}</google-codelab-step>")

    buffer.append("</google-codelab>")
    return ''.join(buffer)

def render(codelab):
    return f'''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, minimum-scale=1.0, initial-scale=1.0, user-scalable=yes">
<title>{codelab.title}</title>

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Code+Pro:400|Roboto:400,300,400italic,500,700|Roboto+Mono">
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://storage.googleapis.com/codelab-elements-tmp/codelab-elements.css">
</head>
<body>
{render_content(codelab)}
<script src="https://storage.googleapis.com/codelab-elements-tmp/native-shim.js"></script>
<script src="https://storage.googleapis.com/codelab-elements-tmp/custom-elements.min.js"></script>
<script src="https://storage.googleapis.com/codelab-elements-tmp/prettify.js"></script>
<script src="https://storage.googleapis.com/codelab-elements-tmp/codelab-elements.js"></script>
</body>
</html>
'''