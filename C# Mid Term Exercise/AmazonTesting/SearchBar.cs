using OpenQA.Selenium;

namespace AmazonTesting
{
    class SearchBar
    {
        private IWebDriver driver;
        public SearchBar(IWebDriver driver)
        {
            this.driver = driver;
            this.Text = string.Empty;
        }

        public string Text
        {
            get
            {
                return this.Text;
            }
            set
            {
                this.driver.FindElement(By.XPath("//input[@id = 'twotabsearchtextbox']")).SendKeys(value);
            }
        }

        public void Click()
        {
            this.driver.FindElement(By.XPath("//input[@id = 'nav-search-submit-button']")).Click();
        }
    }
}
