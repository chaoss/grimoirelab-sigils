<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{% if page.title %}{{ page.title }}{% else %}{{ site.description }}{% endif %}">
    <meta name="author" content="{{site.author}}">
    <title>{% if page.title %}{{ page.title }}{% else %}{{ site.title }}{% endif %}</title>
  </head>
  <body>
    <h1>{{site.title}} by {{site.author}}</h1>
    <ul>
      {% for panel in site.panels %}
      <li><a href="{{panel.url}}">{{panel.name}}</a></li>
      {% endfor %}
    </ul>
  </body>
</html>