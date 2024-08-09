def handle_response(user_message, self) -> str:

    p_message = user_message.lower()

    if p_message == 'hello':
        return "Hey there!"
    
    if p_message == 'burak':
        return 'ananskim'
    
    if p_message == 'sorgu':
        self.send_trendyol_fiyat.start()

    if p_message == 'sorgu bitir':
        self.send_trendyol_fiyat.cancel()
    
    if p_message == 'logs':
        self.send_logs.start()

    if p_message == 'kosmos':
        self.kosmos_get_max_date.start()

    if p_message == 'kosmos job start':
        self.kosmos_get_max_date_job.start()

    if p_message == 'kosmos job cancel':
        self.kosmos_get_max_date_job.cancel()

    if p_message == 'kosmos logs':
        self.send_kosmos_logs.start()
    
    if p_message == 'help':
        self.help.start()

    if p_message == 'eyv':
        SystemExit