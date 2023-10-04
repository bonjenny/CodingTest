const url = "https://wr4a6p937i.execute-api.ap-northeast-2.amazonaws.com/dev"
function getPromise() {
  let inputValue = document.getElementsByClassName("SearchInput__input")[0].value;
  let newUrl = url+"/languages?keyword="+inputValue;
  return fetch(newUrl)
  .then(response => response.json());
}

function searchInput() {
  let promise = getPromise();
  const getData = () => {
    promise.then((appData) => {
      let ulNode = document.getElementsByClassName('Suggestion')[0].firstElementChild;
      ulNode.innerHTML = "";
      let li;
      let textNode;
      let count = 0;
      for (const value of appData) {
        li = document.createElement("li");
        if (count === 0) { li.setAttribute("class", "Suggestion__item--selected")};
        textNode = document.createTextNode(value);
        li.appendChild(textNode);
        ulNode.appendChild(li);
        count += 1;
      }
    });
  };
  getData();
}
function selectLanguage() {
  event.preventDefault(); // 곧 삭제할 것
}
