const fs = require('fs');
const process = require('process');

if (process.argv.length < 3) {
    console.error("请指定文件路径！");
} else {
    const path = process.argv[2];
    const file = fs.readFileSync(path);
    const dict = JSON.parse(file.toString());
    const words = dict.words;

    let count = 0;
    words.forEach(word => {
        if (word.media.content) {
            count += 1;
        }
    });

    console.log("已配图：", count);
    console.log("总量：", words.length);
    console.log("占比：", count / words.length);
}
