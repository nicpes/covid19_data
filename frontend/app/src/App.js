import "./App.css";
import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState([]);
  const [date, setDate] = useState();

  const fetchData = async () => {
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    try {
      const response = await fetch(
        `http://192.168.1.10:5000/total_cases`,
        requestOptions
      );
      if (!response.ok) {
        throw new Error(
          `This is an HTTP error: The status is ${response.status}`
        );
      }
      let actualData = await response.json();
      setData(actualData);
    } catch (err) {
      setData(null);
    }
  };

  const extractDate = () => {
    for (let i in data) {
      console.log(data[i].data);
    }
  };

  useEffect(() => {
    fetchData();
    setDate(extractDate);
  }, []);

  return (
    <div id="app">
      <div id="table-container">
        <p>{date}</p>
        {data &&
          data.map((element, index) => (
            <div id="element" key={index}>
              Regione: {element.nome} - Totale casi: {element.totale}
            </div>
          ))}
      </div>
    </div>
  );
}

export default App;
