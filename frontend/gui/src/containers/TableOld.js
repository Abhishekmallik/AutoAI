import React from 'react';
import classes from './Table.css'
const Table = (props)=>{


    const data  = props.data;
   
    if(Object.keys(data).length===0)
    {
        return null
    }


    
    const keys = Object.keys(data[0])

    return (
        /*classes["scrollable"] +" "+ classes["table-wrapper"]*/
        /*classes["fl-table"]*/

       

        <div className={classes['rendered_html'] + " "+ classes['output_subarea'] + " " + classes['table-designer']}>

        <h1>{props.title}</h1>
        <table  className="dataframe">

            <thead>
                <tr> 
                {
                    
                    keys.map((key)=>{
                        return (<th>{key}</th>)
                    })
                    
                }
                </tr>
            </thead>
            <tbody>

                {
                    data.map((row,index)=>{
                        return(<tr>
                            {
                                Object.values(row).map((val)=>{
                                    return <td>{val}</td>
                                })
                            }
                        </tr>)
                    })
                }

            </tbody>
        </table>
      </div>
    
    );


}


export default Table;