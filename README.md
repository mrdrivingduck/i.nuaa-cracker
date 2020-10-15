# i.nuaa-cracker

🐀 你懂的

---

## About

For automating some jobs on [i.NUAA](https://i.nuaa.edu.cn).

* Daily reporting for health status
* Daily reporting for leaving campus
* ...

## Dependencies

[Selenium with Python3](https://selenium-python.readthedocs.io/).

Browser drivers are also needed:

| Browser | Link                                                         |
| ------- | ------------------------------------------------------------ |
| Chrome  | https://sites.google.com/a/chromium.org/chromedriver/downloads |
| Edge    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| Firefox | https://github.com/mozilla/geckodriver/releases              |
| Safari  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/ |

## Usage

Copy `config/config.json.template` and rename the file to `config.json`. Configure your own information in `config.json`. Then run the script by:

```shell
python src/main.py config/config.json
```

---

## Contributor

<a href="https://github.com/mrdrivingduck/i.nuaa-cracker/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=mrdrivingduck/i.nuaa-cracker" />
</a>

Made with [contributors-img](https://contributors-img.web.app).

## License

[MIT](LICENSE)

---

