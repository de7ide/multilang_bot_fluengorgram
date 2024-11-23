from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        {
            "ru": ("ru", "en"),
            "hi": ("hi", "en"),
            "en": ("en",)
        },
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=["locales/ru/LC_MESSAGE/txt.ftl"])),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=["locales/en/LC_MESSAGE/txt.ftl"])),
            FluentTranslator(
                locale='hi',
                translator=FluentBundle.from_files(
                    locale="hi-IN",
                    filenames=["locales/hi/LC_MESSAGE/txt.ftl"]))
        ],
    )
    return translator_hub