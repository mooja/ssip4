const path = require('path');

module.exports = {
    entry: './ssip4/static/typescript/index.ts',
    module: {
        rules: [
            // Typescript
            {
                test: /\.tsx?$/,
                use: 'awesome-typescript-loader',
                exclude: /node_modules/
            },

            // Sass
            {
                test: /\.s[ac]ss$/,
                use: [{
                    loader: "style-loader" // creates style nodes from JS strings
                }, {
                    loader: "css-loader" // translates CSS into CommonJS
                }, {
                    loader: "sass-loader", // compiles Sass to CSS
                    options: {
                        includePaths: ["ssip4/static/sass"]
                    }
                }]
            },
            // Images      {
            {
                test: /\.(png|jpg|gif)$/,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            emitFile: false
                        }
                    }
                ]
            }
        ]
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js']
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'ssip4/static/js/')
    }
};
