# Introduction

This is a Sublime plugin for converting HTML to javascript string.

# Usage

This plugin is still in development and not released, so you should add this plugin to your Sublime manually.

1. Put the package in your Sublime packages folder, eg. `C:\Program Files\Sublime Text 3\Data\Packages`

2. Select the rows in the file you are editing, then right click and choose `HtmlToString` option.

# Demo

**Convert**

```
<div class="container">
    <div class="row">
        <div class="col-sm-12"></div>
    </div>
</div>
```

**To**

```
'<div class="container">',
    '<div class="row">',
        '<div class="col-sm-12"></div>',
    '</div>',
'</div>'
```