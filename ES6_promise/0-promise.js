const getResponseFromAPI = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("response from api");
    }, 2000);
  });
};

export default getResponseFromAPI;
