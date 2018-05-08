const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production'
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");


module.exports = {
    entry: './ssip4/static/typescript/index.ts',
    optimization: {
        minimizer: [
            new OptimizeCSSAssetsPlugin({})
        ]
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'awesome-typescript-loader',
                exclude: /node_modules/
            },
            {
                test: /\.s[ac]ss$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                            options: {
                                name: '[name].[ext]',
                        }
                    },
                    "css-loader",
                    "sass-loader"
                ]
            },
            {
                test: /\.(png|jpg|gif)$/,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            name: '[name].[ext]',
                            limit: 100,
                            emitFile: false,
                            publicPath: "/static/images"
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin()
    ],
    resolve: {
        extensions: ['.tsx', '.ts', '.js']
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'ssip4/static/js/')
    }
};
