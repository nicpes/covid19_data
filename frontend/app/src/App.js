import "./App.css";
import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState([]);
  const [date, setDate] = useState("");
  let total = 0;

  /* FETCHING DATA FROM MAIN.PY SERVER AND STORING VALUES IN data */

  const fetchData = async () => {
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    try {
      const response = await fetch(
        `http://localhost:5000/total_cases`,
        requestOptions
      );
      if (!response.ok) {
        throw new Error(
          `This is an HTTP error: The status is ${response.status}`
        );
      }
      let actualData = await response.json();
      setData(actualData);
      for (let i in actualData) {
        setDate(actualData[i].data);
      }
    } catch (err) {
      setData(null);
    }
  };

  /* DAY TOTAL CASES */

  const calcTotal = () => {
    for (let i in data) {
      total += data[i].totale;
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  calcTotal();

  /* MAPPING DATA STATE AND GENERATING THE TABLE */

  return (
    <div id="app">
      <div id="table-container">
        <p>Dati relativi al: {date.slice(0, 10)}</p>
        <h2 id="table-title"> Regione - Totale casi</h2>
        {data &&
          data.map((element, index) => (
            <div id="element" key={index}>
              <span id="element-name">{element.nome}</span>
              <span id="element-total">{element.totale}</span>
            </div>
          ))}
        <p>Totale: {total}</p>
      </div>
    </div>
  );
}

export default App;
