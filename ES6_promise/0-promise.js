// Promise
function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      /* disable */
        if (true) {
          resolve();
        } else {
          reject();
        }
        /* enable */
    });
  }
  
  export default getResponseFromAPI;
  
