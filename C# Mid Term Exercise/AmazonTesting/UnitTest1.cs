using OpenQA.Selenium;

namespace AmazonTesting
{
    public class Tests
    {
        IWebDriver driver;

        [OneTimeSetUp]
        public void SetUp()
        {
            driver = BrowserFactory.GetDriver("chrome");
        }

        [Test]
        public void TestMethod()
        {
            Amazon amazon = new Amazon(driver);
            amazon.Pages.Home.SearchBar.Text = "mouse";
            amazon.Pages.Home.SearchBar.Click();
            var items = amazon.Pages.Results.GetResultsBy(new Dictionary<string, string>()
            { 
                {"Price_Lower_Then","50"},
                {"Price_Higher_OR_Equal_Then","10"},
                {"Free_Shipping","true"}
            });

            Assert.Pass();
        }

        [OneTimeTearDown]
        public void TearDown()
        {
            driver.Quit();
        }
    }
}