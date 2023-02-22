# Access Localization

This project is an open source project that helps our developers manage their translation files more efficiently. It is currently available in Persian and English, but we need your help to translate it into other languages!

## Contributing Translations

We are looking for contributors to help us translate this project into other languages. If you are interested in contributing, please follow these steps:
- Clone from this project
- Update excel with new translations
- Create pull request 

Once your pull request has been merged, we will use the `novaday-co/localization_action` GitHub Action to generate the translation files for Laravel, Vue, and Flutter. The generated files will be released as artifacts and made available for download.

## Translating Variables

This project supports variables in translations to allow for easy customization. To use a variable in a translation, enclose the variable name in curly braces. For example, For example : `Hello, {name}` where {name} is a variable.
