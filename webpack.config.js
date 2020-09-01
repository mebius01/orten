const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssnanoPlugin = require('cssnano-webpack-plugin');
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');

module.exports = {
  entry: {
    index: './src/js/index.js',
  },
  output: {
    path: path.resolve(__dirname, 'static/shop'),
    filename: 'js/main.js'
  },
  watch: true,
  watchOptions: {
    ignored: /node_modules/,
  },

  module: {
    rules: [
      // css || sass
      {
        test:/\.(s*)css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
      },
      // file || image
      {
        test: /\.(gif|png|jpe?g|svg)$/i,
        use: [{
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'img/',
            }
          },
          {
            loader: 'image-webpack-loader',
            options: {
              mozjpeg: {
                progressive: true,
                quality: 65
              },
              optipng: {
                enabled: true,
              },
              pngquant: {
                quality: [0.65, 0.90],
                speed: 4
              },
              gifsicle: {
                interlaced: false
              },
              webp: {
                quality: 75
              }
            },
          },
        ],
      },
    ],
  },

  plugins: [
    new CleanWebpackPlugin(),
    new CssnanoPlugin(),
    new MiniCssExtractPlugin({
      filename: 'css/main.css',
    }),
  ]
};