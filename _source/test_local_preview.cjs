const fs=require("node:fs"),path=require("node:path"),vm=require("node:vm"),assert=require("node:assert/strict");
const source=fs.readFileSync(path.join(__dirname,"../assets/local-preview.js"),"utf8");
function run(href){
  const attrs=[{href:"../about/"},{href:"../products/coffee-wood-dog-chew/?request=sample#sizes"},
    {href:"#main"},{href:"../assets/img/photo.webp"},{href:"https://www.winvnint.com/"},
    {"data-success-url":"thank-you/"}];
  const nodes=attrs.map(a=>({hasAttribute:k=>k in a,getAttribute:k=>a[k],setAttribute:(k,v)=>a[k]=v}));
  let queried=false;
  vm.runInNewContext(source,{window:{location:new URL(href)},URL,document:{querySelectorAll:()=>{queried=true;return nodes;}}});
  return {attrs,queried};
}
const live=run("https://vietpaw.com/request-a-quote/");
assert.equal(live.queried,false);assert.equal(live.attrs[0].href,"../about/");
const local=run("file:///D:/Site/request-a-quote/index.html");
assert.equal(local.attrs[0].href,"file:///D:/Site/about/index.html");
assert.equal(local.attrs[1].href,"file:///D:/Site/products/coffee-wood-dog-chew/index.html?request=sample#sizes");
assert.equal(local.attrs[2].href,"#main");assert.equal(local.attrs[3].href,"../assets/img/photo.webp");
assert.equal(local.attrs[4].href,"https://www.winvnint.com/");
assert.equal(local.attrs[5]["data-success-url"],"file:///D:/Site/request-a-quote/thank-you/index.html");
console.log("PASS: clean production links untouched; local directory links, query strings, anchors and success path work without changing assets/external links.");
