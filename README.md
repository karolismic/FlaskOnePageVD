# VIVID HORIZON - single landing page using Flask/Python/HTML (Bootstrap under the [MIT](https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE) license)

## Preview

[![Grayscale Preview](https://getspace.cloud/cloud/s/qbwAYmwLwZ2dSKK)]

## Status

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/StartBootstrap/startbootstrap-grayscale/master/LICENSE)
[![npm version](https://img.shields.io/npm/v/startbootstrap-grayscale.svg)](https://www.npmjs.com/package/startbootstrap-grayscale)
[![dependencies Status](https://david-dm.org/StartBootstrap/startbootstrap-grayscale/status.svg)](https://david-dm.org/StartBootstrap/startbootstrap-grayscale)
[![devDependencies Status](https://david-dm.org/StartBootstrap/startbootstrap-grayscale/dev-status.svg)](https://david-dm.org/StartBootstrap/startbootstrap-grayscale?type=dev)

## Download and Installation

To begin using this template, choose one of the following options to get started:

- [Download the latest release on Start Bootstrap](https://startbootstrap.com/theme/grayscale/)
- Install using npm: `npm i startbootstrap-grayscale`
- Clone the repo: `git clone https://github.com/StartBootstrap/startbootstrap-grayscale.git`
- [Fork, Clone, or Download on GitHub](https://github.com/StartBootstrap/startbootstrap-grayscale)

## Usage

### Step 1

First, create a new folder in the project directory called **templates**. Create a new file in the templates folder naming **“home.html”** or any other name but make sure that the file ending is .html. There you will add the HTML code.

### Step 2

Now create a new file naming it **"main.py"** or any other name but make sure the file ending is .py in the different folder than templates, open it and add the following code:

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')
if __name__ == '__main__':
  app.run()

We are importing **render_template** function provided by the Flask and then rendering our HTML template in the home route.

### Step 3

Make sure you create a new folder named "static" and put your folders "assets", "css", "js", "pug", "scss" in it.

### Step 4

Now, navigate your browser to **localhost:5000** to see the output.

Awesome! You have just rendered an HTML template in the Flask using Python.

### Basic Usage

After downloading, simply edit the HTML and CSS files included with `dist` directory. These are the only files you need to worry about, you can ignore everything else! To preview the changes you make to the code, you can open the `index.html` file in your web browser.

### Advanced Usage

Clone the source files of the theme and navigate into the theme's root directory. Run `npm install` and then run `npm start` which will open up a preview of the template in your default browser, watch for changes to core template files, and live reload the browser when changes are saved. You can view the `package.json` file to see which scripts are included.

#### npm Scripts

- `npm run build` builds the project - this builds assets, HTML, JS, and CSS into `dist`
- `npm run build:assets` copies the files in the `src/assets/` directory into `dist`
- `npm run build:pug` compiles the Pug located in the `src/pug/` directory into `dist`
- `npm run build:scripts` brings the `src/js/scripts.js` file into `dist`
- `npm run build:scss` compiles the SCSS files located in the `src/scss/` directory into `dist`
- `npm run clean` deletes the `dist` directory to prepare for rebuilding the project
- `npm run start:debug` runs the project in debug mode
- `npm start` or `npm run start` runs the project, launches a live preview in your default browser, and watches for changes made to files in `src`

You must have npm installed in order to use this build environment.

## Bugs and Issues

Have a bug or an issue with this template? [Open a new issue](https://github.com/StartBootstrap/startbootstrap-grayscale/issues) here on GitHub or leave a comment on the [theme overview page at Start Bootstrap](https://startbootstrap.com/theme/grayscale/).

## Copyright and License

Copyright 2013-2021 Start Bootstrap LLC. Code released under the [MIT](https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE) license.
