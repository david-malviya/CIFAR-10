import { useState } from 'react'
import './App.css'
import styles from './Style/App.module.css';

function App() {
  const [file, setFile] = useState(null)
  const [result, setResult] = useState('')
  const [imagePreview, setImagePreview] = useState(null)

  function handleUpload(event){
    const selectedFile = event.target.files[0]
    setFile(selectedFile);

    setTimeout(() => {
        setImagePreview(URL.createObjectURL(selectedFile))
    }, 1000)
  }

  async function handlePredict(){
    const formdata = new FormData();

    formdata.append('file', file);

    try{
        const response = await fetch('http://127.0.0.1:5000/classify', {
            method : 'POST',
            body : formdata
        });

        // if (!response.ok) {
        //     throw new Error('Network response was not ok');
        // }
        const data = await response.json();

        setResult(data['result'] || data['message'] || "no result found!!")

    }catch(error){
        console.error('Error uploading Image', error);
    }
  }


  return (
      <div id={styles.mainContainer}>
          <h1>CIFAR-10 Classification Model</h1>
          <div className={styles.inputFile}>
              <input type="file" onChange={handleUpload}/>
              <button onClick={handlePredict}>Predict</button>
          </div>

          {/*<div className={styles.result}>*/}
          {/*    <p>Result : {result}</p>*/}
          {/*    {*/}
          {/*        imagePreview && (*/}
          {/*            <div className={styles.imagePreview}>*/}
          {/*                <h3>Image Preview</h3>*/}
          {/*                <img src={imagePreview} alt="Preview not available"/>*/}
          {/*            </div>*/}
          {/*        )*/}
          {/*    }*/}
          {/*</div>*/}


          <div className={styles.result}>
              <p>Result : {result}</p>
                      <div className={styles.imagePreview}>
                          <h3>Image Preview </h3>
                          {
                            imagePreview && (
                            <img src={imagePreview} alt="Preview not available"/>
                          )
                          }
              </div>
          </div>

      </div>
  )
}

export default App
