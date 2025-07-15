"use strict";

{
  const btn = document.querySelector('.btn');
  const container = document.querySelector('.container');

  btn.addEventListener('click', () => {
    btn.classList.toggle('active');
    container.classList.toggle('active');

  });

    document.getElementById('scrollToBottom').addEventListener('click', function () {
    window.scrollTo({
      top: document.body.scrollHeight,
      behavior: 'smooth' // アニメーション付き
    });
  });
}