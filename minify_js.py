import rjsmin

input_file = "app_formatted-v2.js"
output_file = "app_minify-v2.js"

with open(input_file, "r", encoding="utf-8") as f:
    data = f.read()

minified = rjsmin.jsmin(data)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(minified)

print("Done ->", output_file)
