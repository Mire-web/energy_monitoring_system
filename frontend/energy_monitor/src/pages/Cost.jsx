import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import './../styles/Cost.css';

const data = [
  { time: '0hrs', electricity: 0.1, gas: 0 },
  { time: '1hrs', electricity: 0.1, gas: 0 },
  { time: '2hrs', electricity: 0.1, gas: 0 },
  { time: '3hrs', electricity: 0.1, gas: 0 },
  { time: '4hrs', electricity: 0.1, gas: 0 },
  { time: '5hrs', electricity: 0.1, gas: 0 },
  { time: '6hrs', electricity: 0.1, gas: 0 },
  { time: '7hrs', electricity: 0.1, gas: 0 },
  { time: '8hrs', electricity: 0.2, gas: 0.1 },
  { time: '9hrs', electricity: 0.3, gas: 0.1 },
  { time: '10hrs', electricity: 0.4, gas: 0.2 },
  { time: '11hrs', electricity: 0.1, gas: 0 },
  { time: '12hrs', electricity: 0.4, gas: 0.2 },
  { time: '13hrs', electricity: 0.4, gas: 0.3 },
  { time: '14hrs', electricity: 0.4, gas: 0.4 },
  { time: '15hrs', electricity: 0.4, gas: 0.3 },
  { time: '16hrs', electricity: 0.4, gas: 0.3 },
  { time: '17hrs', electricity: 0.3, gas: 0.2 },
];

function Cost() {
  return (
    <div className="cost-page">
      <div className="time-selector">
        <button className="active">TODAY</button>
        <button>MONTH</button>
        <button>YEAR</button>
      </div>
      <h2>COST</h2>
      <div className="cost-stats">
        <div className="stat">
          <h3>TODAY</h3>
          <p>JAN 22ND 2025</p>
          <p className="value">$7.1</p>
        </div>
        <div className="stat">
          <h3>SO FAR TODAY</h3>
          <p className="value">$1.55</p>
        </div>
        <div className="stat">
          <h3>PREDICTED TODAY</h3>
          <p className="value">$6.2</p>
        </div>
        <div className="stat">
          <h3>ESTIMATED SAVINGS</h3>
          <p className="value">$0.9</p>
        </div>
      </div>
      <div className="cost-chart">
        <BarChart
          width={600}
          height={300}
          data={data}
          margin={{
            top: 5, right: 30, left: 20, bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="electricity" fill="#82ca9d" name="Electricity" stackId="a" />
          <Bar dataKey="gas" fill="#ffc658" name="Gas" stackId="a" />
        </BarChart>
      </div>
      <div className="date-display">January, 23rd 2025</div>
    </div>
  );
}

export default Cost;
