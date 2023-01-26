using OpenQA.Selenium;

namespace AmazonTesting
{
    class Amazon
    {
        private IWebDriver driver;
        private Pages pages;

        public Amazon(IWebDriver driver)
        {
            this.driver = driver;
            this.driver.Navigate().GoToUrl("https://www.amazon.com/");
        }

        public Pages Pages
        {
            get
            {
                if (this.pages == null)
                {
                    this.pages = new Pages(this.driver);
                }
                return this.pages;
            }
        }
    }
}
