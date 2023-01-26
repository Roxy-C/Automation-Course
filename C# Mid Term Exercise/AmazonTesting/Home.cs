using OpenQA.Selenium;

namespace AmazonTesting
{
    class Home
    {
        private IWebDriver _driver;
        private SearchBar _searchBar;

        public Home(IWebDriver driver)
        {
            this._driver = driver;
        }

        public SearchBar SearchBar
        {
            get
            {
                if (this._searchBar == null)
                {
                    this._searchBar = new SearchBar(this._driver);
                }
                return this._searchBar;
            }
        }
    }
}
