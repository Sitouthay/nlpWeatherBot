- create environment with conda
	conda create --name rasa

- activate conda environment
	conda activate rasa

- install rasa stack
	conda install rasa

- run rasa
	rasa run actions
	rasa run --endpoints endpoints.yml --credentials credentials.yml

- run ngrok server
	ngrok http 5005

+ connect rasa with messenger
token: ---
secret app: ---
name: ---

+ connect rasa with whatsapp
token: ---
secret app: ---
name: ---




