from api import app

# get photos
@app.get('/api/photo')
async def get_all_or_exact_photo(photo_id: int =0, user_id: int =0):
    pass

# get photo of exact user
@app.put('/api/photo')
async def change_user_photo():
    pass

#delete  user photo
@app.delete('/api/photo')
async def delete_user_photo():
    pass
