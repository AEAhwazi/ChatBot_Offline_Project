import streamlit as st
import AI

detail = False

st.title("WelCome To Olamma AI")

if st.sidebar.button('New Chat'):
    st.session_state.clear()
    st.sidebar.success("New chat starting...")

if st.sidebar.button('Clear Chat History'):
    st.session_state.clear()
    st.sidebar.success('All chat history clear...')
    st.session_state['messages'] = [{'role': 'AI', 'content': "I Am AI, How Can I Help You?"}]

if st.sidebar.checkbox('View Detail'):
    detail = True
    st.sidebar.success('View answer AI with detail...')

if st.sidebar.button('Copy chat to file'):
    path = f'chat_file.txt'
    file = open(path, 'w', encoding='utf-8')
    for msg in st.session_state['messages']:
        role = msg.get('role', 'unknown')
        content = msg.get('content', '')
        file.write(f'{role}: {content}\n')
        line = '-' * 50
        file.write(f'{line}\n')

    st.sidebar.success(f'The history chat saved in {path}')
    file.close()

if st.sidebar.button('View history file chat'):
    path = 'chat_file.txt'
    file = open(path, 'r', encoding='utf-8')
    history_chat = file.read()
    
    st.sidebar.download_button(
        label='Download / View file',
        data=history_chat,
        file_name=path,
        mime='text/plan'
    )
    file.close()
    
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role': 'AI', 'content': 'I Am AI, How Can I Help You?'}]
    
for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])
    
prompt = st.chat_input("Please Enter Your Question? ")
model = 'gemma3:1b'

if prompt:

    st.chat_message('User').write(prompt)

    st.session_state['messages'].append({'role': 'USER', 'content': prompt})

    with st.spinner('Genarating Response...'):
        if detail:
            new_prompt = prompt + 'Describe your answer with detail and shape'
            answer = AI.call_ollama_model(new_prompt, model)

        else:
            answer = AI.call_ollama_model(prompt, model)
    
        st.chat_message('AI').write(answer)
        st.session_state['messages'].append({'role': 'AI', 'content': answer})
    

    