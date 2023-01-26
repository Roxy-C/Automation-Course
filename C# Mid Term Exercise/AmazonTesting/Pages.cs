using OpenQA.Selenium;

namespace AmazonTesting
{
    class Pages
    {
        private IWebDriver _driver;
        private Home _home;
        private Results _results; 

        public Pages(IWebDriver driver)
        {
            this._driver = driver;
        }

        public Home Home
        {
            get
            {
                if (this._home == null)
                {
                    this._home = new Home(this._driver);
                }
                return this._home;
            }
        }

        public Results Results
        {
            get
            {
                if (this._results == null)
                {
                    this._results = new Results(this._driver);
                }
                return this._results;
            }
        }
    }
}
