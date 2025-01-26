// src/components/Appliance.js

import './../styles/UsageByRoom.css';

const data = [
  { room: 'Master Bedroom', usage: [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2] },
  { room: 'Bedroom 1', usage: [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3] },
  { room: 'Drawing Room', usage: [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2] },
  { room: 'Living Room', usage: [2, 3, 2, 1, 0, 1, 2, 3, 4, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1] },
  { room: 'Kitchen', usage: [3, 2, 1, 0, 1, 2, 3, 4, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 3] },
  { room: 'Garage', usage: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
  { room: 'Others', usage: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] }
];

function UsageByRoom() {
  return (
    <div className="usage-page">
      <div className="time-selector">
        <button className="active">THIS MONTH</button>
        <button>LAST MONTH</button>
      </div>
      <h2>USAGE BY ROOMS</h2>
      <div className="heatmap-container">
        {data.map((item, index) => (
          <div key={index} className="room-row">
            <div className="room-label">{item.room}</div>
            <div className="heatmap">
              {item.usage.map((value, idx) => (
                <div key={idx} className={`heatmap-cell usage-${value}`}>
                  {value === 5 && (
                    <div className="prediction-label">
                      Predicted: Kitchen<br />Jan 21: 2KWh
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
      <div className="legend">
        <div className="legend-item"><span className="usage-0"></span> 0 - 1KWh</div>
        <div className="legend-item"><span className="usage-1"></span> 1 - 2KWh</div>
        <div className="legend-item"><span className="usage-2"></span> 2 - 3KWh</div>
        <div className="legend-item"><span className="usage-3"></span> 3 - 4KWh</div>
        <div className="legend-item"><span className="usage-4"></span> &gt;4KWh</div>
      </div>
    </div>
  );
}

export default UsageByRoom;
