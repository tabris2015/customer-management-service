# env variables
export FIRESTORE_EMULATOR_HOST="localhost:8080"
export GOOGLE_APPLICATION_CREDENTIALS="/home/pepe/dev/DigitalRealState/fastapi-todo-app/KEY.json"
# run firestore emulator
firebase emulators:start &

# run server
python -m app.main