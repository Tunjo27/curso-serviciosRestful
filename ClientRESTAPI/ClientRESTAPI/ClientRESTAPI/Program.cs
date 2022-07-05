using System;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace ClientRESTAPI
{
    public class User
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    class Program
    {
        static HttpClient client = new HttpClient();

        static void ShowUser(User user)
        {
            Console.WriteLine($"Name: {user.Name} \tCategory: {user.Age }");
        }

        static async Task<User> GetUserAsync(string path)
        {
            User user = null;
            HttpResponseMessage response = await client.GetAsync(path);
            if (response.IsSuccessStatusCode)
            {
                user = await response.Content.ReadAsAsync<User>();
            }
            return user;
        }

        static void Main()
        {
            RunAsync().GetAwaiter().GetResult();
        }

        static async Task RunAsync()
        {
            try
            {
                User user = await GetUserAsync("http://localhost:8082/");
                ShowUser(user);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.ReadLine();
        }
    }
}
