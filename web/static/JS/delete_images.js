const configPath = '../../Pdf_to_Notion/PdfToImage/config.json';

// JSONファイルを非同期に読み込む
fetch(configPath)
  .then(response => {
    if (!response.ok) {
      throw new Error('設定ファイルの読み込みに失敗しました。');
    }
    return response.json();
  })
  .then(data => {
    const isServer = data.server[0].is_server;
    if (!isServer) {
      // is_serverがfalseの場合(ローカルの場合)、ボタンを表示
      const deleteButton = document.getElementById("deleteButton");
      deleteButton.style.display = "block"; // ボタンを表示
    } else {
      const deleteButton = document.getElementById("deleteButton");
      deleteButton.style.display = "none"; // ボタンを非表示
    }
  })
  .catch(error => {
    console.error('設定ファイルの読み込みエラー:', error);
  });
    


function deleteImages() {
    // サーバーサイドのコマンドを実行するためのHTTPリクエストを送信
    fetch('/delete_images', {
        method: 'POST', 
    })
    .then(response => {
        // レスポンスを処理
        if (response.ok) {
            showMessage('画像の削除が成功しました。');
        } else {
            showMessage('画像の削除に失敗しました。');
        }
    })
    .catch(error => {
        showMessage('エラーが発生しました。', 'error');
        console.error('エラーが発生しました。', error);
    });
}

