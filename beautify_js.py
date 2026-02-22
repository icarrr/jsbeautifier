import jsbeautifier

input_file = "app.js"
output_file = "app_formatted.js"

with open(input_file, "r", encoding="utf-8") as f:
    data = f.read()

opts = jsbeautifier.default_options()
opts.indent_size = 4

formatted = jsbeautifier.beautify(data, opts)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted)

print("Done ->", output_file)
