using OpenQA.Selenium;
using System.Reflection;

namespace AmazonTesting
{
    class Results
    {
        private IWebDriver _driver;

        public Results(IWebDriver driver)
        {
            this._driver = driver;
        }

        public List<Item> GetResultsBy(Dictionary<String, String> filters)   //return List of items
        {
            List<Item> resultsItems = new List<Item>();
            string baseXpath = "//span[@class = 'a-price'";

            if (filters == null || filters.Count == 0)
            {
                return resultsItems;
            }

            if (filters.Count > 0)
            {
                foreach (var filter in filters)
                {
                    switch (filter.Key.ToLower())
                    {
                        case "price_lower_then":
                            baseXpath += " and concat(descendant::span[@class = 'a-price-whole']//text() ,'.',descendant::span[@class='a-price-fraction']//text()) < " + filter.Value;
                            break;

                        case "price_lower_or_equal_then":
                            baseXpath += " and concat(descendant::span[@class = 'a-price-whole']//text() ,'.',descendant::span[@class='a-price-fraction']//text()) <= " + filter.Value;
                            break;

                        case "price_higher_then":
                            baseXpath += " and concat(descendant::span[@class = 'a-price-whole']//text() ,'.',descendant::span[@class='a-price-fraction']//text()) > " + filter.Value;
                            break;

                        case "price_higher_or_equal_then":
                            baseXpath += " and concat(descendant::span[@class = 'a-price-whole']//text() ,'.',descendant::span[@class='a-price-fraction']//text()) >= " + filter.Value;
                            break;

                        case "price_equal_to":
                            baseXpath += " and concat(descendant::span[@class = 'a-price-whole']//text() ,'.',descendant::span[@class='a-price-fraction']//text()) = " + filter.Value;
                            break;

                        case "free_shipping":
                            if ((filter.Value).ToLower() == "true")
                            {
                                baseXpath += " and (ancestor::div[@class = 'a-section a-spacing-small a-spacing-top-small']//descendant::span[@class = 'a-color-base a-text-bold'])";
                            }
                            else
                            {
                                baseXpath += " and not(ancestor::div[@class = 'a-section a-spacing-small a-spacing-top-small']//descendant::span[@class = 'a-color-base a-text-bold'])";
                            }
                            break;
                    }
                }
            }

            
            var relevantResults = this._driver.FindElements(By.XPath(baseXpath + ']'));

            foreach (var result in relevantResults)
            {
                IList<IWebElement> title = result.FindElements(By.XPath("ancestor::div[@class = 'a-section']//span[@class = 'a-size-medium a-color-base a-text-normal']"));
                IList<IWebElement> url = result.FindElements(By.XPath("ancestor::div[@class = 'a-section']//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"));
                string price = result.Text;

                if (title.Count == 0 || url.Count == 0)
                {
                    title = result.FindElements(By.XPath("ancestor::li[@class = 'a-carousel-card']//span[@class = 'a-size-base-plus a-color-base a-text-normal']"));
                    url = result.FindElements(By.XPath("ancestor::li[@class = 'a-carousel-card']//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"));
                }

                if (title.Count == 0 || url.Count == 0)
                {
                    title = result.FindElements(By.XPath("ancestor::div[@class = 'sg-col-inner']//span[@class = 'a-size-medium a-color-base a-text-normal']"));
                    url = result.FindElements(By.XPath("ancestor::div[@class = 'sg-col-inner']//a[@class = 'a-link-normal a-text-normal']"));
                }

                Item tempItem = new Item(title[0].Text, url[0].GetAttribute("href"), price);
                Console.WriteLine(tempItem.toString());
                resultsItems.Add(tempItem);
            }

            return resultsItems;
        }
    }
}
