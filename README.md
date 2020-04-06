
# xlsxtpl
A python module to generate xlsx files from a xlsx template.


## How it works

xlsxtpl uses openpyxl to read and write .xlsx files, uses jinja2 as its template engine.  
When xlsxtpl reads a .xlsx file, it creates a tree for each worksheet.  
Then, it translates the tree to a jinja2 template with custom tags.  
When the template is rendered, jinja2 extensions of cumtom tags call corresponding tree nodes to write the .xlsx file.  

## Syntax

xlsxtpl uses jinja2 as its template engine, follows the [syntax of jinja2 template](https://jinja.palletsprojects.com/).  

Each worksheet is translated to a jinja2 template with custom tags.  

```jinja2
...
...
{% row 45 %}
{% cell 46 %}{% endcell %}
{% cell 47 %}{% endcell %}
{% cell 48 %}{{address}}  {%xv v%}{% endcell %}
{% cell 49 %}{% endcell %}
{% cell 50 %}{% endcell %}
{% cell 51 %}{% endcell %}
{% cell 52 %}{% endcell %}
{% cell 53 %}{% endcell %}
{% row 54 %}
{% cell 55 %}{% endcell %}
{% cell 56 %}{% sec 0 %}{{name}}{% endsec %}{% sec 1 %}{{address}}{% endsec %}{% endcell %}
...
...
{% for item in items %}
{% row 64 %}
{% cell 65 %}{% endcell %}
{% cell 66 %}{% endcell %}
{% cell 67 %}{% endcell %}
{% cell 68 %}{% endcell %}
{% cell 69 %}{% endcell %}
{% cell 70 %}{% endcell %}
{% cell 71 %}{% endcell %}
{% cell 72 %}{% endcell %}
{% endfor %}
...
...

```

xlsxtpl added 4 custom tags: row, cell, sec, and xv.  
row, cell, sec are used internally, used for row, cell and rich text.  
xv is used to define a variable.   
When a cell contains only a xv tag, this cell will be set to the type of the object returned from the variable evaluation.  
For example, if a cell contains only {%xv amt %}, and amt is a number, then this cell will be set to Number type, displaying with the style set on the cell.  
If there is another tag, it is equivalent to {{amt}}, will be converted to a string.  



## Installtion

```shell
pip install xlsxtpl
```

## How to use

See [examples](https://github.com/zhangyu836/python-xlsx-template/tree/master/examples).

## Notes

### Rich text

Openpyxl does not preserve the rich text it read. 
A temporary workaround for rich text is provided in [this repo](https://bitbucket.org/zhangyu836/openpyxl/) ([2.6](https://bitbucket.org/zhangyu836/openpyxl/src/2.6/)).
For now, xlsxtpl uses this repo to support rich text reading and writing.

