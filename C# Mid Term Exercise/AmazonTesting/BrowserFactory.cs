using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Edge;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium;

namespace AmazonTesting
{
    class BrowserFactory
    {
        private static string _pathComputer = "C:\\WebDrivers";

        public static IWebDriver GetDriver(string browser)
        {
            IWebDriver driver;
            switch (browser.ToLower())
            {
                case "chrome":
                    ChromeOptions options = new ChromeOptions();
                    options.AddArguments("--incognito");
                    driver = new ChromeDriver(_pathComputer, options);
                    break;
                case "firefox":
                    driver = new FirefoxDriver(@"C:\WebDriver\geckodriver.exe");
                    break;
                case "edge":
                    driver = new EdgeDriver(_pathComputer);
                    break;
                default:
                    throw new ArgumentException("Invalid browser type");
            }
            return driver;
        }

        public static void CloseDriver(IWebDriver driver)
        {
            driver.Quit();
        }
    }
}
