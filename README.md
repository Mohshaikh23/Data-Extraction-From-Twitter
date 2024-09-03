# Twitter/X User Data Scraper

This repository contains a Python script that automates the process of scraping user data from Twitter (X). The script uses Selenium and BeautifulSoup to extract various data points, including user names, usernames, follower counts, following counts, joining dates, and recent tweets.

## Features

- **Automated Web Scraping**: Automates the process of scraping data from Twitter (X) profiles.
- **Data Extraction**: Extracts and stores user names, usernames, follower counts, following counts, number of posts, banner and profile picture URLs, and up to five of the most recent tweets.
- **Error Handling**: Implements robust error handling for missing elements, ensuring that the script continues to run even if some data points are not found.
- **CSV Output**: Stores the scraped data in a CSV file for easy analysis and sharing.

## Requirements

Before running the script, ensure that you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (Make sure it matches your Chrome version)

### Python Packages

You can install the required Python packages using `pip`:

```bash
pip install pandas beautifulsoup4 selenium
```

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Mohshaikh23/Data-Extraction-From-Twitter.git
   ```

2. **Prepare the Input File**:

   Create a text file named `abc.txt` in the root directory of the project. This file should contain the Twitter/X usernames you want to scrape, one per line.

   Example of `abc.txt`:

   ```
   @elonmusk
   @nasa
   @google
   ```

3. **Run the Script**:

   Execute the Python script:

   ```bash
   python_scrapper.py
   ```

   The script will open a Chrome browser window, navigate to each user's profile, and extract the specified data.

4. **Output**:

   After the script completes, a CSV file named `Fetched_Data.csv` will be generated in the root directory containing the scraped data.

   ![Image]('E:\END TO END ML PROJECT\Data-Extraction-From-Twitter\Screenshot 2024-09-04 002651.png')

## Notes

- **Login Required**: If the profiles you are scraping require you to be logged in, you will need to uncomment the login section in the script and provide your credentials.
- **Timeouts**: The script includes `time.sleep()` commands to handle loading times. You may need to adjust these values based on your internet speed.
- **Error Handling**: The script is designed to continue running even if some data points are missing or cannot be found.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This script is for educational purposes only. Please respect Twitter's/X's [terms of service](https://help.twitter.com/en/rules-and-policies/twitter-rules) and use the script responsibly.

## Contact

For any questions or issues, please open an issue on this repository or contact me at [mohsin.shaikh324@gmail.com].
