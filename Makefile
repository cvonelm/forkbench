default:
	{% for file in files %}
	gcc -lm -O0 {{file}}.c -o {{file}}
	{% endfor %}
clean:
	{% for file in files %}
	rm {{file}}.c
	rm {{file}}
	{% endfor %}
