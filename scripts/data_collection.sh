url="https://disk.yandex.com/d/EgOiWzvrh9qLIg"

wget "$(yadisk-direct $url)" -O data/data.zip

unzip data/data.zip -d data/
cp data/toy-data/*.csv data/
rm -rf data/toy-data
rm data/data.zip