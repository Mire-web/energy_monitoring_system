// import React from 'react';
import '../styles/Dashboard.css';

import {
  PieChart, Pie, Cell,
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Text,
  AreaChart, Area, ReferenceLine,
//   Tooltip, 
  ResponsiveContainer
} from 'recharts';

const Dashboard = () => {
  const data = [
    { name: 'Jan', energy: 4000 },
    { name: 'Feb', energy: 3000 },
    { name: 'Mar', energy: 2000 },
    { name: 'Apr', energy: 2780 },
    { name: 'May', energy: 1890 },
    { name: 'Jun', energy: 2390 },
    { name: 'Jul', energy: 3490 },
  ];
  const pie_data = [
    { name: 'Group A', value: 400 },
    { name: 'Group B', value: 300 },
    { name: 'Group C', value: 300 },
    { name: 'Group D', value: 200 },
  ];
  const change_in_cost_data = [
    { name: 'Dec', cost: 203 },
    { name: 'Jan', cost: 214 },
  ];
  const usage_data = [
    { name: 'Jan', actual: 120.16, predicted: 120.16 },
    { name: 'Feb', actual: null, predicted: 200 },
    { name: 'Mar', actual: null, predicted: 300 },
    { name: 'Apr', actual: null, predicted: 460 },
  ];
  const appliances_data = [
    { name: 'Heating & AC', value: 1.4 },
    { name: 'EV Charge', value: 0.9 },
    { name: 'Plug Loads', value: 0.8 },
    { name: 'Refrigeration', value: 0.7 },
    { name: 'Lighting', value: 0.4 },
    { name: 'Others', value: 0.2 },
  ];
  const guage_data = [
    { value: 70 }, // Value displayed in the gauge
    { value: 30 }, // Remaining part of the circle
  ];
  const progress_data1 = [
    {
      name: 'Emission',
      tillDate: 36.4,
      predicted: 181.8,
      tillDateLabel: '36.4 Kg of CO2',
      predictedLabel: '181.8 Kg of CO2',
      value: 40,
    }
  ];
  const guage_color = ['#22E412', '#ccc'];
  const chartValue = 47;
//   const dummy_data = [
//     {
//         name: 'Energy Usage',
//         value: 75,
//       },
//   ]
  
  // Colors for the pie sections
    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];
    const total = pie_data.reduce((sum, entry) => sum + entry.value, 0);
    const percentageChange = (
        (change_in_cost_data[1].cost - change_in_cost_data[0].cost) / change_in_cost_data[0].cost * 100).toFixed(2);

  return (
    <div className="dashboard metric-area">
        {/* Predicted Cost */}
        <section className='metric-card'>
            <div className='title'>
                <h4>COST PREDICTED</h4>
            </div>
            <ResponsiveContainer width="100%" height={300} className={'cost-predicted'}>
                <PieChart>
                    <Pie
                    data={pie_data}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={80}
                    fill="#8884d8"
                    paddingAngle={5}
                    dataKey="value"
                    label
                    >
                    {data.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                    </Pie>
                    <text 
                    x="50%" 
                    y="50%" 
                    textAnchor="middle" 
                    dominantBaseline="middle"
                    style={{ fontSize: '24px', fontWeight: 'bold', fill: '#FFFFFF' }}
                    >
                    {total}
                    </text>
                </PieChart>
                </ResponsiveContainer>
        </section>
        {/* Change in Cost */}
        <section className='metric-card'>
            <div className='title'>
                <h4>CHANGE IN COST</h4>
            </div>
            <ResponsiveContainer width="100%" height={300} className={'change-in-cost'}>
                <BarChart data={change_in_cost_data} margin={{ top: 25, right: 30, left: 10, bottom: 5 }}
                style={{ height: 280 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#ccc"  />
                    <XAxis dataKey="name" stroke="white" />
                    <YAxis tickFormatter={(value) => `$${value}`} stroke="white" />
                    <Tooltip />
                    <Bar dataKey="cost" fill="#00C49F" barSize={30} label={{ position: 'insideTop', fill: '#FFFFFF' }}>
                    {data.map((entry, index) => (
                        <Text key={`value-${index}`} x={index * 150 + 75} y={0} textAnchor="middle" verticalAnchor="start" fill="white">
                        ${entry.cost}
                        </Text>
                    ))}
                    </Bar>
                </BarChart>
                <div style={{display: 'flex', alignItems: 'center', flexDirection: 'column', justifyContent: 'center',
                    marginRight: '20px', width: '20%'
                }}>
                    <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'row'}}>
                        <span style={{ color: '#FF5733', fontSize: '1.5rem' }}>▲</span>
                        <span style={{ marginLeft: '5px', color: '#FF5733', fontSize: '1.5rem' }}>{percentageChange}%</span>
                    </div>
                    <div style={{ marginLeft: '5px', color: '#ffffff', fontSize: '0.8rem', textWrap: 'nowrap' }}>INCREASE IN COST</div>
                </div>
            </ResponsiveContainer>
        </section>
        {/* Usage Estimate */}
        <section className='metric-card'>
            <div className='title'>
                <h4>USAGE ESTIMATE</h4>
            </div>
            <ResponsiveContainer height={300} className={'usage-estimate'}>
                <div className='usage-estimate-description'
                style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px', 
                    width: '80%', padding: '0 20px'
                }}>
                    <span>Till Now: 120.16 kWh</span>
                    <span>Predicted: 460 kWh</span>
                </div>
                <AreaChart data={usage_data} margin={{ top: 25, right: 30, left: 2, bottom: 5 }} 
                 style={{ width: '90%' }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
                    <XAxis dataKey="name" stroke="white" />
                    <YAxis tickFormatter={(value) => `${value} kWh`} stroke="white" />
                    <Tooltip />
                    
                    {/* Actual usage */}
                    <Area 
                    type="monotone" 
                    dataKey="actual" 
                    stroke="#FF5733" 
                    fill="#FF5733" 
                    fillOpacity={0.8} 
                    name="Actual"
                    />
                    
                    {/* Predicted usage */}
                    <Area 
                    type="monotone" 
                    dataKey="predicted" 
                    stroke="#00C49F" 
                    fill="#00C49F" 
                    fillOpacity={0.3} 
                    name="Predicted"
                    />
                    
                    {/* Reference line to show current month */}
                    <ReferenceLine x="Jan" stroke="white" strokeDasharray="3 3" />
                    <ReferenceLine y={120.16} stroke="white" strokeDasharray="3 3" />
                    
                    {/* Adding dots for each point */}
                    {data.map((entry, index) => (
                    <ReferenceLine 
                        key={`dot-${index}`} 
                        x={entry.name} 
                        y={entry.predicted} 
                        stroke="red" 
                        strokeWidth={2} 
                        if={entry.actual === null}
                    />
                    ))}
                </AreaChart>
            </ResponsiveContainer>
        </section>
        {/* Active Appliances */}
        <section className='metric-card'>
            <div className='title'>
                <h4>ACTIVE APPLIANCES</h4>
            </div>
            <ResponsiveContainer width="100%" height={300} className={'active-appliances'}>
                <BarChart data={appliances_data} layout="vertical" margin={{ top: 5, right: 30, left: -2, bottom:0 }}
                style={{ width: '100%'}}>
                    {/* <CartesianGrid strokeDasharray="3 3" stroke="#ccc" /> */}
                    <XAxis type="number" tickFormatter={(value) => `${value} kWh`} stroke="white" />
                    <YAxis type="category" dataKey="name" width={100} stroke="white" />
                    <Tooltip />
                    <Bar dataKey="value" fill="#8E44AD" barSize={30}>
                    {data.map((entry, index) => (
                        <Text 
                        key={`value-${index}`} 
                        x={410} 
                        y={index * 50 + 25} 
                        textAnchor="start" 
                        verticalAnchor="middle" 
                        fill="white"
                        >
                        {`${entry.value} kWh`}
                        </Text>
                    ))}
                    </Bar>
                </BarChart>
                <div style={{ marginTop: '0', fontSize: '12px', color: '#ffffff', textAlign: 'center' }}>
                    Top 3 appliances make up <strong>70.3%</strong> of the net usage.
                </div>
            </ResponsiveContainer>
        </section>
        {/* Energy Intensity */}
        <section className='metric-card'>
            <div className='title'>
                <h4>ENERGY INTENSITY</h4>
            </div>
            <ResponsiveContainer height={300} className={'guage-chart'}>
                <PieChart margin={{ top: 40, right: 0, left: 0, bottom:0 }} className='guage'
                style={{ width: '100%'}}>
                    <Pie
                        data={guage_data}
                        dataKey="value"
                        strokeWidth={0}
                        startAngle={180} // Start at the bottom (semi-circle)
                        endAngle={0} // End at the top (semi-circle)
                        innerRadius="80%" // Inner empty circle to make it a gauge
                        outerRadius="100%" // Outer circle radius
                        paddingAngle={0} // Optional spacing between segments
                    >
                        {data.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={guage_color[index]} />
                        ))}
                    </Pie>
                </PieChart>
                <div style={{ display:'flex', marginTop: '0', fontSize: '12px', color: '#ffffff', 
                   }}
                    className='guage-value'>
                    <p style={{ fontSize: '2rem', margin: '0' }}>{chartValue}</p>
                    <p style={{ fontSize: '1rem', margin: '0' }}>kWh/Sqft</p>
                </div>
            </ResponsiveContainer>
        </section>
        {/* Carbon Footprint */}
        <section className='metric-card progress-card'>
            <div className='title'>
                <h4>CARBON FOOTPRINT</h4>
            </div>
            
            <ResponsiveContainer width="100%" height={20}  className={'progress-chart1'}>
                <div className='emission-info'>
                    <p>{progress_data1[0]['name']}</p>
                    <div className='emission-info-labels'>
                        <p>Till Date</p>
                        <p>Predicted</p>
                    </div>
                </div>
                <BarChart data={progress_data1} layout="vertical"
                margin={{top: 0, bottom: 5,}} style={{ marginTop: '0px', marginBottom: '0px',
                    padding: '0px',
                }}>
                    <XAxis type="number" domain={[0, 100]} hide/>
                    <YAxis dataKey="name" type="category" width={10} hide/>
                    <Tooltip />
                    <Bar dataKey="value" fill="#8884d8" background={{ fill: '#eee' }} 
                    barSize={10}/>
                </BarChart>
                <div className='emission-info-values'>
                    <p>{progress_data1[0]['tillDateLabel']}</p>
                    <p>{progress_data1[0]['predictedLabel']}</p>
                </div>

                <div className='emission-info2'>
                    <p>Green Energy Generated</p>
                </div>            
                <BarChart data={progress_data1} layout="vertical"
                margin={{top: 0, bottom: 0,}} style={{ marginTop: '-15px', marginBottom: '0px',
                    padding: '0px',
                }}>
                    <XAxis type="number" domain={[0, 100]} hide/>
                    <YAxis dataKey="name" type="category" width={10} hide/>
                    <Tooltip />
                    <Bar dataKey="value" fill="#8884d8" background={{ fill: '#eee' }} 
                    barSize={10}/>
                </BarChart>
                <div className='emission-info-values2'>
                    <p>21.20 kWh</p>
                </div>
            </ResponsiveContainer>
        </section>
    </div>
  );
};

export default Dashboard;
