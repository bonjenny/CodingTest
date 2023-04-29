export const API_END_POINT =
  "https://wr4a6p937i.execute-api.ap-northeast-2.amazonaws.com/dev";

const request = async (url) => { // async
  const res = await fetch(url); // await

  if (res.ok) {
    const json = await res.json();
    return json;
  }
  throw new Error("요청에 실패함");
};

export const fetchLanguages = async (keyword) =>
  request(`${API_END_POINT}/languages?keyword=${keyword}`);
