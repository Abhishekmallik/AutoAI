import React from 'react';
import classes from './Table.css'
const TabelComponet = (props)=>{

    
    const data = props.data 

    if(data === undefined || Object.keys(data).length===0)
    {
        return null
    }


    const columns =data["columns"]

    const index = data["index"]

    const value = data["data"]



    let rows = []

    for(var i = 0 ;i<value.length;i++)
    {
        let row = [<th>{index[i]}</th>]
        for(var j=0;j<value[i].length;j++)
        {
            row.push(<td>{value[i][j]}</td>)
        }
        rows.push(row);
    }


    return (
        <div className={classes['rendered_html'] + " "+ classes['output_subarea']}>
            <h1>{props.title}</h1>
            <table>
                <thead>
                    <tr>
                        <th>

                        </th>

                        {
                            columns.map((column)=>{
                                return <th>{column}</th>
                            })
                        }
                    </tr>
                    
                </thead>

                <tbody>

                    
                            {Object.values(rows).map((value)=>{
                                return <tr>{value}</tr>
                            })}
                    
                </tbody>
            </table>

        </div>


    )


}

export default TabelComponet;