using OpenQA.Selenium;

namespace AmazonTesting
{
    class Item
    {
        private string _title { get; set; }
        private string _url { get; set; }
        public string price { get; set; }

        public Item(string title, string url, string price)
        {
            this._title = title;
            this._url = url;
            this.price = price.Replace("$", "").Replace("\r\n", ".");
        }

        public string toString()
        {
            return this._title + ", " + this._url + ", " + this.price;
        }
    }
}
