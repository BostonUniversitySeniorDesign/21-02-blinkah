## Frontend Run Instructions

-   Install NodeJs from  [NodeJs Official Page](https://nodejs.org/en/?ref=creativetim)
-   Open Terminal
-   Go to your file project (where you've unzipped the product)
-   Navigate to frontend
-   Run in terminal
    
    ```
    npm install
    ```
    
-   Then run
    
    ```
    npm start
    ```
    
    If you have an error something containing
    
    ```
    Module not found
    ```
    
    You should check if in your root project folder you have a file named  `.env`.  
    If you do not have it, then create it and add this line in it:  `NODE_PATH=./src`  
    If that does not work, you need to do the following
    
    ```
    npm install --g cross-env
    ```
    
    then change the  `script`  inside  `package.json`  by adding  `NODE_PATH=./src`  inside it. For example, the start script would be changed from
    
    ```
    "start": "react-scripts start",
    ```
    
    to
    
    ```
    "start": "NODE_PATH=./src react-scripts start",