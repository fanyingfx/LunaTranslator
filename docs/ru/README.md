
# Инструкция по настройке LunaTranslator

<p align="left">
    <a href=../images/ru//LICENSE"><img src="https://img.shields.io/badge/license-GPL%203.0-dfd.svg"></a>
    <a href="https://github.com/HIllya51/LunaTranslator/releases"><img src="https://img.shields.io/github/v/release/HIllya51/LunaTranslator?color=ffa"></a>
    <a href="https://github.com/HIllya51/LunaTranslator/stargazers"><img src="https://img.shields.io/github/stars/HIllya51/LunaTranslator?color=ccf"></a>
     
</p> 
 
<a id="table1"></a>

## Основные функции:

#### Выбор источника текста

&emsp;&emsp;**Буфер обмена** Копирование текста из буфера обмена для перевода.

&emsp;&emsp;**OCR** Поддерживает автономные считывальщики текста с экрана Paddle OCR и WindowsOCR, а также онлайн сервисы: Baidu OCR, Youdao OCR, OCRspace, docsumo. Также поддерживает привязку и скрытие окон для распознавания текста с экрана для удобной игры.

&emsp;&emsp;**HOOK** Поддерживает использование HOOK для получения текста из данных игры, поддерживает использование специальных кодов, поддерживает автоматическое сохранение игр, а также автоматическую загрузку HOOK во время запуска игр.


#### Выбор переводчика

Поддерживает почти все существующие механизмы перевода, в том числе:

&emsp;&emsp;**Автономный перевод** Поддержка автономного перевода с использованием JBeijing 7, Jinshan Quick Translation и Yidiantong (Не работает для перевода на русский язык).

&emsp;&emsp;**Бесплатный онлайн-перевод** Поддержка Baidu, Bing, Google, Ali, Youdao, Caiyun, Sogou, DeepL, Kingsoft, Xunfei, Tencent, Byte, Volcano, papago, yeekit и других онлайн-сервисов.

&emsp;&emsp;**Онлайн-перевод с регистрацией ключа API** Поддержка перевода с использованием зарегистрированных пользователем ключей перевода для Baidu, Tencent, Youdao, Mavericks, Caiyun, Volcano, Deepl и других.

&emsp;&emsp;**Предварительный перевод** Поддержка чтения файлов предварительного перевода, выполненных человеком, и агрегация машинных файлов.

&emsp;&emsp;**Поддержка пользовательских расширений перевода** Поддержка использования языка python для расширения других интерфейсов перевода, о которых я не знаю.

#### Синтез речи/Озвучка текста

&emsp;&emsp;**Offline TTS** Поддержка windowsTTS, VoiceRoid2 и VOICEVOX.

&emsp;&emsp;**Online TTS** Поддержка AzureTTS и Volcano TTS.

#### Обработка текста/Оптимизация перевода

&emsp;&emsp;**Обработка текста** Поддерживает простую обработку, такую, как дедупликация текста, фильтрация HTML-тегов, фильтрация разрывов строк, фильтрация символов и чисел, поддержка пользовательской простой замены текста и замены с использованием регулярных выражений.

&emsp;&emsp;**Оптимизация перевода** Поддерживает использование собственных корректировок перевода и импорт общих словарей VNR.

#### Японская письменность

&emsp;&emsp;**Сегментация японских слов и отображение каны** Поддержка использования встроенных бесплатных загружаемых инструментов сегментации слов и отображения каны, поддержка использования Mecab для оптимизации сегментации слов и отображения каны, поддержка сторонних словарей.

&emsp;&emsp;**Поиск слов** Поддержка поиска слов с использованием Xiaoxiaoguan, Lingoes Dictionary и EDICT (японо-английский словарь).
