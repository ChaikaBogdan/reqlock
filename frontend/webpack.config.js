const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const {EnvironmentPlugin} = require('webpack');

module.exports = {
  entry: "./index.js",
  output: {
    path: path.join(__dirname, "/static/frontend"),
    filename: "bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      },
      {
        test: /\.s?css$/,
        use: [
          "style-loader",
          "css-loader",
          "sass-loader",
       ],
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({title: 'ReqLock', template: './index.html'}),
    new EnvironmentPlugin({BACKEND_URL: 'http://127.0.0.1:8000'})
  ]
};