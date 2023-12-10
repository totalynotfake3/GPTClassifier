# GPTClassifier
Classifier for psychological Disorders based on a fixed MongoDB and GPT API

# To Do's:
1. Windows installation guide


# Instructions for DB

For Mac OS:
1. Install xcode via terminal with : xcode-select --install
2. Install brew via terminal with : /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3. Download MongoDB via brew : brew tap mongodb/brew
4. Update to most recent version : brew update
5. Install the MongoDB Community version: brew install mongodb-community@7.0
6. Start the MongoDB brew services start mongodb-community@7.0
7. Recommended : Install MongoDB Compass for UI :
   https://www.mongodb.com/try/download/compass
8. Via the MongoDB Compass  -> Create new database and collection
9. Import the New.New JSON Data to import the database
10. Change the OpenAI Api Key to your personal one in the .env section of this git
11. Run the code and see the classification results

   
