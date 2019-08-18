export const success = {
    statusCode: 200,
    isBase64Encoded: false,
    headers: {},
    body: ""
  };
  
  
  export const invalid = (error: Error) => ({
    statusCode: 400,
    isBase64Encoded: false,
    headers: {},
    body: error.message
  });